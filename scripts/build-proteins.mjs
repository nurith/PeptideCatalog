#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { parse } from 'csv-parse/sync';

const csvPath = path.resolve(process.cwd(), 'file.csv');
const outPath = path.resolve(process.cwd(), 'src/data/proteins.ts');

function normalizeCell(value) {
  return String(value ?? '')
    .replace(/\u00a0/g, ' ')
    .trim();
}

function toBoolean(value) {
  return ['1', 'true', 'yes', 'y'].includes(normalizeCell(value).toLowerCase());
}

function titleSlug(value) {
  return normalizeCell(value)
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '') || 'entry';
}

if (!fs.existsSync(csvPath)) {
  throw new Error(`Missing CSV source: ${csvPath}`);
}

const rows = parse(fs.readFileSync(csvPath, 'utf8'), {
  bom: true,
  relax_column_count: true,
  skip_empty_lines: true,
  trim: false,
});

const dataRows = rows.slice(1);

const records = dataRows.map((row, index) => {
  // The CSV has nine fields. Pad short rows and preserve any extra trailing
  // fields as part of the final sequence-entry field.
  const values = [...row];
  while (values.length < 9) values.push('');
  if (values.length > 9) {
    values.splice(8, values.length - 8, values.slice(8).join(','));
  }

  const [
    peptideDb,
    uniprot,
    endonet,
    fragments,
    hormone,
    propeptide,
    transcript,
    entry,
    sequence,
  ] = values;

  const title = normalizeCell(entry) || `Peptide record ${index + 1}`;
  const rowId = String(index + 1).padStart(4, '0');

  return {
    id: rowId,
    // Keep the row number at the end so long titles cannot truncate it.
    slug: `${titleSlug(title).slice(0, 72)}-${rowId}`,
    title,
    peptideDb: normalizeCell(peptideDb),
    uniprot: normalizeCell(uniprot),
    endonet: normalizeCell(endonet),
    fragments: toBoolean(fragments),
    hormone: toBoolean(hormone),
    propeptide: toBoolean(propeptide),
    transcript: toBoolean(transcript),
    // This CSV column may contain FASTA headers as well as sequences.
    sequence: normalizeCell(sequence),
  };
});

const content = `export type ProteinRecord = {
  id: string;
  slug: string;
  title: string;
  peptideDb: string;
  uniprot: string;
  endonet: string;
  fragments: boolean;
  hormone: boolean;
  propeptide: boolean;
  transcript: boolean;
  sequence: string;
};

export const proteins: ProteinRecord[] = ${JSON.stringify(records, null, 2)};
`;

fs.mkdirSync(path.dirname(outPath), { recursive: true });
fs.writeFileSync(outPath, content, 'utf8');

console.log(`Generated ${records.length} protein records.`);