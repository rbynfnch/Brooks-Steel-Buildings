// Merges data/auto/*.json (pulled from Google) with data/manual/*.json (typed by you / reported by Brooks)
// into data/data.js, which index.html loads. Works when opened straight from disk (no server).
// Usage: node scripts/build-data.mjs
import { readdirSync, readFileSync, writeFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const read = (p) => JSON.parse(readFileSync(p, 'utf8'));
const keys = readdirSync(join(root, 'data/auto')).filter((f) => f.endsWith('.json')).map((f) => f.slice(0, 7)).sort();

const months = keys.map((k) => {
  const auto = read(join(root, 'data/auto', `${k}.json`));
  const mp = join(root, 'data/manual', `${k}.json`);
  const manual = existsSync(mp) ? read(mp) : {};
  return { ...auto, ...manual, sample: Boolean(auto.sample || manual.sample) };
});

writeFileSync(join(root, 'data/data.js'), `window.DASHBOARD_DATA = ${JSON.stringify({ site: 'brookssteelbuildings.com', months })};\n`);
console.log(`Built data/data.js with ${months.length} months (${months.at(-1)?.month}).`);
