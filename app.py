from flask import Flask, jsonify, request

app = Flask(__name__)

products = [
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
    },
]
next_id = 4


# ============================================================
# Routes
# ============================================================

@app.route("/api/products", methods=["GET"])
def get_all_products():
    """Mengambil seluruh daftar produk."""
    return jsonify({
        "status": "success",
        "data": products
    }), 200


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """Mengambil detail satu produk berdasarkan ID."""
    product = next((p for p in products if p["id"] == product_id), None)

    if product is None:
        return jsonify({
            "status": "error",
            "message": "Produk tidak ditemukan"
        }), 200 

    return jsonify({
        "status": "success",
        "data": product
    }), 200


@app.route("/api/products", methods=["POST"])
def create_product():
    """Membuat produk baru."""
    global next_id
    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Request body tidak boleh kosong"
        }), 400

    required_fields = ["name", "price", "category", "stock"]
    for field in required_fields:
        if field not in data or data[field] is None:
            return jsonify({
                "status": "error",
                "message": f"Field '{field}' wajib diisi"
            }), 400

    # Validasi tipe data
    if not isinstance(data["name"], str) or len(data["name"].strip()) == 0:
        return jsonify({
            "status": "error",
            "message": "Field 'name' harus berupa string dan tidak boleh kosong"
        }), 400

    if not isinstance(data["price"], (int, float)):
        return jsonify({
            "status": "error",
            "message": "Field 'price' harus berupa angka"
        }), 400

    if not isinstance(data["stock"], int):
        return jsonify({
            "status": "error",
            "message": "Field 'stock' harus berupa bilangan bulat"
        }), 400

    if data["stock"] < 0:
        return jsonify({
            "status": "error",
            "message": "Field 'stock' tidak boleh bernilai negatif"
        }), 400

    new_product = {
        "id": next_id,
        "name": data["name"],
        "price": data["price"],
        "category": data["category"],
        "stock": data["stock"]
    }
    next_id += 1
    products.append(new_product)

    return jsonify({
        "status": "success",
        "message": "Produk berhasil ditambahkan",
        "data": new_product
    }), 200  


@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """Memperbarui data produk yang sudah ada."""
    product = next((p for p in products if p["id"] == product_id), None)

    if product is None:
        return jsonify({
            "status": "error",
            "message": "Produk tidak ditemukan"
        }), 404

    data = request.get_json()
    if not data:
        return jsonify({
            "status": "error",
            "message": "Request body tidak boleh kosong"
        }), 400

    if "name" in data:
        product["name"] = data["name"]
    if "price" in data:
        if data["price"] < 0:
            return jsonify({
                "status": "error",
                "message": "Field 'price' tidak boleh bernilai negatif"
            }), 400
        product["price"] = data["price"]
    if "category" in data:
        product["category"] = data["category"]
    if "stock" in data:
        if data["stock"] < 0:
            return jsonify({
                "status": "error",
                "message": "Field 'stock' tidak boleh bernilai negatif"
            }), 400
        product["stock"] = data["stock"]

    return jsonify({
        "status": "success",
        "message": "Produk berhasil diperbarui",
        "data": product
    }), 200


@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """Menghapus produk berdasarkan ID."""
    global products
    product = next((p for p in products if p["id"] == product_id), None)

    if product is None:
        return jsonify({
            "status": "error",
            "message": "Produk tidak ditemukan"
        }), 404

    products = [p for p in products if p["id"] != product_id]

    return jsonify({
        "status": "success",
        "message": "Produk berhasil dihapus"
    }), 200


# ============================================================
# Entry point
# ============================================================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
