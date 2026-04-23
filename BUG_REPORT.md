# Bug Report — TechMart API

## ✅ Endpoints That Meet the Specification
- `GET /api/products` — Passes.
- `PUT /api/products/{product_id}` — Passes.
- `DELETE /api/products/{product_id}` — Passes.

## ❌ Bugs Found

### Bug #1: GET product not found returns 200 instead of 404
- **Endpoint:** `GET /api/products/{product_id}`
- **Reproduction Steps:** Send GET request to `/api/products/999` (non-existent ID)
- **Expected Result:** HTTP status `404 Not Found` with error message
- **Actual Result:** HTTP status `200 OK` is returned instead of `404`

### Bug #2: POST new product returns 200 instead of 201
- **Endpoint:** `POST /api/products`
- **Reproduction Steps:** Send POST to `/api/products` with valid body `{"name":"Mouse","price":150000,"category":"Aksesoris","stock":10}`
- **Expected Result:** HTTP status `201 Created`
- **Actual Result:** HTTP status `200 OK` is returned instead of `201`

### Bug #3: POST with negative price returns 200 instead of 400
- **Endpoint:** `POST /api/products`
- **Reproduction Steps:** Send POST to `/api/products` with `{"name":"Mouse","price":-100,"category":"Aksesoris","stock":10}`
- **Expected Result:** HTTP status `400 Bad Request` with message `"Field 'price' tidak boleh bernilai negatif"`
- **Actual Result:** HTTP status `200 OK` and product is created successfully — no validation for negative price