## ✅ Endpoints That Meet the Specification

- `GET /api/products` — Passes. Returns `200 OK` with the full product list correctly.
- `PUT /api/products/{product_id}` — Passes. Returns `200 OK` on success, `404 Not Found` when product is missing, and correctly validates negative `price` and `stock`.
- `DELETE /api/products/{product_id}` — Passes. Returns `200 OK` on success and `404 Not Found` when product is missing.

## ❌ Bugs Found

### Bug #1: Wrong HTTP Status Code on "Product Not Found" for GET Single Product

- **Endpoint:** `GET /api/products/{product_id}`
- **Reproduction Steps:** Send a `GET` request to `/api/products/999` (a non-existent ID) using the following command:- **Expected Result:** According to the specification, the response status code should be `404 Not Found` with body:
```json
  {
    "status": "error",
    "message": "Produk tidak ditemukan"
  }
```
- **Actual Result:** The API returns status code `200 OK` instead of `404 Not Found`. The response body message is correct, but the HTTP status code does not match the specification.

### Bug #2: Wrong HTTP Status Code on Successful Product Creation

- **Endpoint:** `POST /api/products`
- **Reproduction Steps:** Send a valid `POST` request to `/api/products` with a complete JSON body using the following command:- **Expected Result:** According to the specification, a successful product creation should return `201 Created` with body:
```json
  {
    "status": "success",
    "message": "Produk berhasil ditambahkan",
    "data": {
      "id": 4,
      "name": "Wireless Mouse",
      "price": 350000,
      "category": "Aksesoris",
      "stock": 50
    }
  }
```
- **Actual Result:** The API successfully creates the product and returns the correct response body, but the HTTP status code is `200 OK` instead of `201 Created`.


### Bug #3: Missing Validation for Negative Price on POST

- **Endpoint:** `POST /api/products`
- **Reproduction Steps:** Send a `POST` request to `/api/products` with a negative `price` value using the following command:- **Expected Result:** According to the specification, the API should reject this request with `400 Bad Request` with body:
```json
  {
    "status": "error",
    "message": "Field 'price' tidak boleh bernilai negatif"
  }
```
- **Actual Result:** The API accepts the request and successfully creates the product with a negative price. Product with `id: 5` and `price: -99999` was created. No validation is applied for negative `price` values in the `POST` endpoint, unlike the `PUT` endpoint which correctly rejects negative prices.
```json
  {
    "data": {
      "category": "Test",
      "id": 5,
      "name": "Test Bug",
      "price": -99999,
      "stock": 1
    },
    "message": "Produk berhasil ditambahkan",
    "status": "success"
  }
```