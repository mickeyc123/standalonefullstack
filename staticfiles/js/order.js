document.addEventListener('DOMContentLoaded', function () {
    // Initial declarations
    var cart = [];
    var total = 0;
    const orderList = document.getElementById("order-list");
    const orderTotal = document.getElementById("order-total");

    // Function to render the cart
    function renderCart() {
        if (!orderList || !orderTotal) {
            console.error('orderList or orderTotal element not found.');
            return;
        }

        orderList.innerHTML = "";

        cart.forEach((item, index) => {
            const li = document.createElement("li");
            let sizeText = '';
            if (item.size) {
                sizeText = `Size: ${item.size} (${item.sizeLetter})`; // Display size with size letter
            }
            li.innerHTML = `
                <img src="${item.image}" width="50" height="50">
                <span>${item.name}</span>
                <span>${sizeText}</span>
                <span>&pound;${item.price.toFixed(2)}</span>
                <button class="remove-item-btn" data-index="${index}">Remove</button>`;
            orderList.appendChild(li);
        });

        orderTotal.textContent = total.toFixed(2);
        attachRemoveButtonEvents();
        updateCartCount(); // Update the cart count display
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
            total -= cart[index].price;
            cart.splice(index, 1);
            renderCart();
            saveCartToStorage(); // Save the updated cart to local storage
        }
    }

    // Function to handle adding items to cart
    function addToCart(type, id, name, price, image, size) {
        let sizeLetter = ''; // Default size letter
        if (size === 'M') {
            sizeLetter = 'M'; // If size is 'M', set size letter to 'M'
        } else if (size === 'L') {
            sizeLetter = 'L'; // If size is 'L', set size letter to 'L'
        }
        cart.push({ type, id, name, price, size, sizeLetter, image });
        total += price;
        renderCart();
        saveCartToStorage(); // Save the updated cart to local storage
    }

    // Event listener for "Add to Cart" buttons
    document.querySelectorAll('.add-to-cart').forEach(button => {
        button.addEventListener('click', function () {
            const type = this.getAttribute('data-type');
            const id = this.getAttribute('data-id');
            const name = this.getAttribute('data-name');
            let price = parseFloat(this.getAttribute('data-price'));
            const image = this.getAttribute('data-image');

            // Get the selected size ('M' or 'L')
            let size = 'M'; // Default size to 'M'
            const sizeRadioButtons = document.querySelectorAll(`input[name="size${id}"]`);
            sizeRadioButtons.forEach(radioButton => {
                if (radioButton.checked) {
                    size = radioButton.value;
                    // Update price based on size
                    if (size === 'M') {
                        price = parseFloat(this.getAttribute('data-price-m'));
                    } else if (size === 'L') {
                        price = parseFloat(this.getAttribute('data-price-l'));
                    }
                }
            });

            addToCart(type, id, name, price, image, size);
        });
    });

    // Function to update the cart count display
    function updateCartCount() {
        const cartCount = document.getElementById("pcart");
        cartCount.textContent = cart.length;
    }

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


   
