import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

// Single source of truth for the landing-page application list.
// The file also lives in `public/` so it is served at /app-menu.json,
// and is read here at build time so the table can be server-rendered.
const __dirname = path.dirname(fileURLToPath(import.meta.url));

export default function () {
	const file = path.join(__dirname, "..", "public", "app-menu.json");
	return JSON.parse(fs.readFileSync(file, "utf-8"));
}
