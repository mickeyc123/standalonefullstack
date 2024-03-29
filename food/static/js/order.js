document.addEventListener('DOMContentLoaded', function () {
    // Initial declarations
    var cart = [];
    var total = 0;
    const orderList = document.getElementById("order-list");
    const orderTotal = document.getElementById("order-total");
    const cartCount = document.getElementById("pcart");

    // Function to render the cart
    function renderCart() {
        orderList.innerHTML = "";
        cart.forEach((item, index) => {
            const li = document.createElement("li");
            li.innerHTML = `<img src="${item.image}" width="50" height="50"> ${item.name} - &pound;${item.price.toFixed(2)}
                        <button class="remove-item-btn" data-index="${index}">Remove</button>`; // Added "Remove" button
            orderList.appendChild(li);
        });
        orderTotal.textContent = total.toFixed(2);
        cartCount.textContent = cart.length;
        saveCartToStorage();
        attachRemoveButtonEvents(); // Ensures event listeners are attached
    }
    function attachRemoveButtonEvents() {
        document.querySelectorAll('.remove-item-btn').forEach(button => {
            button.addEventListener('click', function (event) {
                const index = parseInt(event.target.getAttribute('data-index'), 10);
                removeFromCart(index);
            });
        });
    }
    function removeFromCart(index) {
        if (index >= 0 && index < cart.length) {
            total -= cart[index].price; // Deduct the price of the removed item from the total
            cart.splice(index, 1); // Remove the item from the cart
            renderCart(); // Re-render the cart to reflect the change
        }
    }

    // Function to handle adding items to cart
    function addToCart(type, id, name, price, image) {
        cart.push({ type, id, name, price, image });
        total += price;
        renderCart();
    }

    // Function to handle removing items from cart
    // Presumably implemented elsewhere or to be implemented

    // Event listener for "Add to Cart" buttons
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function () {
            const type = this.getAttribute('data-type');
            const id = this.getAttribute('data-id');
            const name = this.getAttribute('data-name');
            let price = parseFloat(this.getAttribute('data-price'));
            const image = this.getAttribute('data-image');

            if (['pizza', 'burger'].includes(type)) {
                const size = document.querySelector(`input[name="size${id}"]:checked`).value;
                price = parseFloat(this.getAttribute(`data-price-${size.charAt(0)}`));
            }

            addToCart(type, id, name, price, image);
        });
    });

    cartCount.textContent = cart.length;

    // Local Storage functions
    function saveCartToStorage() {
        localStorage.setItem('cart', JSON.stringify(cart));
        localStorage.setItem('total', total.toString());
    }

    function loadCartFromStorage() {
        try {
            const storedCart = localStorage.getItem('cart');
            const storedTotal = localStorage.getItem('total');
            if (storedCart && storedTotal) {
                cart = JSON.parse(storedCart);
                total = parseFloat(storedTotal);
                renderCart();
            }
        } catch (error) {
            console.error("Error loading the cart from localStorage:", error);
            cart = [];
            total = 0;
        }
    }

    // Initialize cart from localStorage
    loadCartFromStorage();
});
