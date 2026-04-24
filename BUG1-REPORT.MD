# Bug Report — TechMart API

## ✅ Endpoints That Meet the Specification
- GET /api/products — Passes
- PUT /api/products/{product_id} — Passes
- DELETE /api/products/{product_id} — Passes

## ❌ Bugs Found
### Bug #1 — GET /api/products/{id} returns 200 instead of 404
### Bug #2 — POST /api/products returns 200 instead of 201
### Bug #3 — POST /api/products accepts negative price