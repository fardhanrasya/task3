## 📘 Spesifikasi API — TechMart Product Catalog

**Base URL:** `http://localhost:5000`

API ini mengelola data **Produk** pada toko online TechMart. Setiap produk memiliki atribut berikut:

| Field      | Tipe     | Keterangan                              |
|------------|----------|-----------------------------------------|
| `id`       | Integer  | ID unik produk (auto-generated)         |
| `name`     | String   | Nama produk (wajib, tidak boleh kosong) |
| `price`    | Number   | Harga produk (wajib, **tidak boleh bernilai negatif**) |
| `category` | String   | Kategori produk (wajib)                 |
| `stock`    | Integer  | Jumlah stok (wajib, tidak boleh negatif)|

> **Catatan:** API ini menggunakan *in-memory storage*. Data akan kembali ke kondisi awal setiap kali *container* di-*restart*.

---

### 1️⃣ Mendapatkan Semua Produk

|             |                     |
|-------------|---------------------|
| **Method**  | `GET`               |
| **Path**    | `/api/products`     |

**Response Sukses — `200 OK`:**
```json
{
  "status": "success",
  "data": [
    {
      "id": 1,
      "name": "Laptop Gaming Pro X1",
      "price": 15500000,
      "category": "Laptop",
      "stock": 10
    },
    {
      "id": 2,
      "name": "Mechanical Keyboard RGB",
      "price": 875000,
      "category": "Aksesoris",
      "stock": 25
    },
    {
      "id": 3,
      "name": "Monitor UltraWide 34 inch",
      "price": 7200000,
      "category": "Monitor",
      "stock": 5
    }
  ]
}
```

---

### 2️⃣ Mendapatkan Detail Produk

|             |                              |
|-------------|------------------------------|
| **Method**  | `GET`                        |
| **Path**    | `/api/products/{product_id}` |

**Response Sukses — `200 OK`:**
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "name": "Laptop Gaming Pro X1",
    "price": 15500000,
    "category": "Laptop",
    "stock": 10
  }
}
```

**Response Gagal (produk tidak ditemukan) — `404 Not Found`:**
```json
{
  "status": "error",
  "message": "Produk tidak ditemukan"
}
```

---

### 3️⃣ Membuat Produk Baru

|                |                              |
|----------------|------------------------------|
| **Method**     | `POST`                       |
| **Path**       | `/api/products`              |
| **Content-Type** | `application/json`        |

**Request Body:**
```json
{
  "name": "Wireless Mouse Ergo",
  "price": 350000,
  "category": "Aksesoris",
  "stock": 50
}
```

**Aturan Validasi:**
- Semua *field* (`name`, `price`, `category`, `stock`) **wajib diisi**.
- `name` harus berupa *string* dan tidak boleh kosong.
- `price` harus berupa angka dan **tidak boleh bernilai negatif**.
- `stock` harus berupa bilangan bulat dan **tidak boleh negatif**.

**Response Sukses — `201 Created`:**
```json
{
  "status": "success",
  "message": "Produk berhasil ditambahkan",
  "data": {
    "id": 4,
    "name": "Wireless Mouse Ergo",
    "price": 350000,
    "category": "Aksesoris",
    "stock": 50
  }
}
```

**Response Gagal (validasi gagal) — `400 Bad Request`:**
```json
{
  "status": "error",
  "message": "Field 'price' tidak boleh bernilai negatif"
}
```

---

### 4️⃣ Memperbarui Produk

|                |                              |
|----------------|------------------------------|
| **Method**     | `PUT`                        |
| **Path**       | `/api/products/{product_id}` |
| **Content-Type** | `application/json`        |

**Request Body** (kirim hanya *field* yang ingin diperbarui):
```json
{
  "price": 14000000,
  "stock": 8
}
```

**Aturan Validasi:**
- `price` (jika dikirim) **tidak boleh bernilai negatif**.
- `stock` (jika dikirim) **tidak boleh negatif**.

**Response Sukses — `200 OK`:**
```json
{
  "status": "success",
  "message": "Produk berhasil diperbarui",
  "data": {
    "id": 1,
    "name": "Laptop Gaming Pro X1",
    "price": 14000000,
    "category": "Laptop",
    "stock": 8
  }
}
```

**Response Gagal (produk tidak ditemukan) — `404 Not Found`:**
```json
{
  "status": "error",
  "message": "Produk tidak ditemukan"
}
```

---

### 5️⃣ Menghapus Produk

|             |                              |
|-------------|------------------------------|
| **Method**  | `DELETE`                     |
| **Path**    | `/api/products/{product_id}` |

**Response Sukses — `200 OK`:**
```json
{
  "status": "success",
  "message": "Produk berhasil dihapus"
}
```

**Response Gagal (produk tidak ditemukan) — `404 Not Found`:**
```json
{
  "status": "error",
  "message": "Produk tidak ditemukan"
}
```
