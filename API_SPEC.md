# API spec

Routes:

- Random Pokemon in a given region
  - Region is name (e.g. "Kanto", check `pokedex`)
  - Returns...
    - Name (species name via `species-list` in "en")
    - id (POKEMON ID, not pokedex number, so check `pokedex`)
    - types (string list)
    - egg cycles (check `species-list` under "hatch_counter")

EXAMPLE INPUT

```json
{
  "region": "Paldea"
}
```

EXAMPLE OUTPUT

```json
{
  "name": "tatsugiri",
  "id": "978",
  "types": ["dragon", "ice"],
  "egg_cycles": "35"
}
```
