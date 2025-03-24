// static/js/script.js
// Cart functionality
let cart = JSON.parse(localStorage.getItem('cart')) || [];

function addToCart(productId) {
    const quantity = parseInt(document.getElementById('quantity').value);
    const product = {
        id: productId,
        name: `Product ${productId}`,
        price: 45.00, // Example price
        quantity: quantity
    };

    const existingProduct = cart.find(item => item.id === productId);
    if (existingProduct) {
        existingProduct.quantity += quantity;
    } else {
        cart.push(product);
    }

    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    alert('Product added to cart!');
}

function updateCartCount() {
    const cartCount = cart.reduce((total, item) => total + item.quantity, 0);
    document.getElementById('cart-count').textContent = cartCount;
}

function displayCart() {
    const cartItems = document.getElementById('cart-items');
    const cartTotal = document.getElementById('cart-total');
    cartItems.innerHTML = '';

    let total = 0;
    cart.forEach(item => {
        const itemTotal = item.price * item.quantity;
        total += itemTotal;
        cartItems.innerHTML += `
            <tr>
                <td>${item.name}</td>
                <td>£${item.price.toFixed(2)}</td>
                <td>${item.quantity}</td>
                <td>£${itemTotal.toFixed(2)}</td>
                <td><button class="btn btn-danger btn-sm" onclick="removeFromCart(${item.id})">Remove</button></td>
            </tr>
        `;
    });

    cartTotal.textContent = `£${total.toFixed(2)}`;
}

function removeFromCart(productId) {
    cart = cart.filter(item => item.id !== productId);
    localStorage.setItem('cart', JSON.stringify(cart));
    updateCartCount();
    displayCart();
}

// Search functionality (mock)
document.querySelector('form').addEventListener('submit', function(e) {
    e.preventDefault();
    const query = document.getElementById('q').value.toLowerCase(); // Fixed: Added query retrieval
    const results = [
        { id: 1, name: "Men's Casual Shirt", price: 35.00 },
        { id: 2, name: "Women's Floral Dress", price: 50.00 },
        { id: 3, name: "Kids' Denim Jacket", price: 25.00 }
    ].filter(item => item.name.toLowerCase().includes(query));

    const searchResults = document.getElementById('search-results');
    if (searchResults) { // Added null check
        searchResults.innerHTML = '';
        results.forEach(item => {
            searchResults.innerHTML += `
                <div class="col-md-4 mb-4">
                    <div class="card product-card">
                        <img src="{% static 'img/product1.jpg' %}" class="card-img-top" alt="${item.name}">
                        <div class="card-body">
                            <h5 class="card-title">${item.name}</h5>
                            <p class="card-text">£${item.price.toFixed(2)}</p>
                            <a href="{% url 'product' product_id=${item.id} %}" class="btn btn-primary">View Details</a>
                        </div>
                    </div>
                </div>
            `;
        });
    }
});

// Initialize cart on page load
document.addEventListener('DOMContentLoaded', function() {
    updateCartCount();
    if (document.getElementById('cart-items')) {
        displayCart();
    }
});