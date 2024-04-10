// Function to handle cart and orders
function shoppingCart() {
    var orders = JSON.parse(localStorage.getItem('cart'));
    var total = localStorage.getItem('total');
    var cartSize = orders ? orders.length : 0;

    var nameElement = document.querySelector("#name");
    var sizeElement = document.querySelector("#size");
    var priceElement = document.querySelector("#price");
    var billElement = document.querySelector("#total");

    nameElement.textContent = 'Name';
    sizeElement.textContent = 'Size';
    priceElement.textContent = 'Price (£)';

    var totalPrice = 0; // Initialize total price variable

    for (let i = 0; i < cartSize; i++) {
        var button = '<button class="del" onclick="removeItem(' + i + ')">Remove</button>';
        nameElement.innerHTML += '<h4>' + orders[i].name + '</h4>';
        let sizeText = orders[i].size === 'M' ? 'Medium' : 'Large';
        sizeElement.innerHTML += '<h4>' + sizeText + '</h4>';
        priceElement.innerHTML += '<h4>£' + orders[i].price.toFixed(2) + button + '</h4>';

        totalPrice += orders[i].price; // Add current item's price to total
    }

    billElement.innerHTML = '<h2>Total: £' + totalPrice.toFixed(2) + '</h2>'; // Display total price

    // Update the total in localStorage as well
    localStorage.setItem('total', totalPrice.toFixed(2));
}

function removeItem(index) {
    var orders = JSON.parse(localStorage.getItem('cart'));

    // Remove the item from the orders array
    orders.splice(index, 1);

    // Save the updated orders array back to localStorage
    localStorage.setItem('cart', JSON.stringify(orders));

    // Call shoppingCart again to update the display
    shoppingCart();
}

document.addEventListener('DOMContentLoaded', function () {
    shoppingCart(); // Call the shoppingCart function when the page loads
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
function orders() {
    console.log('Order function called');

    var msg = document.querySelector('#message').value;
    var orders = JSON.parse(localStorage.getItem('cart'));
    var address = document.querySelector('#address').value; // Get the address field value

    console.log('Message:', msg);
    console.log('Orders:', orders);
    console.log('Address:', address);

    // Check if 'orders' is an array
    if (!Array.isArray(orders)) {
        console.error("'orders' is not an array or is empty.");
        return;
    }

    var url = submitOrderUrl; // Use the {% url %} template tag
    var orderData = {
        'orders': orders,
        'note': msg,
        'address': address // Include address in orderData
    };

    var csrftoken = getCookie('csrftoken');

    console.log('Order Data:', orderData);

    $.ajax({
        url: url ,
        type: 'POST',
        headers: {
            'X-CSRFToken': csrftoken
        },
        data: JSON.stringify(orderData),
        contentType: 'application/json',
        success: function (data) {
            console.log('Order successful:', data);
            // Redirect to success page after successful order
            window.location.href = '/food/success/';
            // Clear cart and total from localStorage
            localStorage.setItem('cart', JSON.stringify([]));
            localStorage.setItem('total', 0);
        },
        error: function (xhr, status, error) {
            console.error('Error:', xhr.responseText);
            // Handle errors here
        }
    });
}

document.addEventListener('DOMContentLoaded', function () {
    shoppingCart(); // Call the shoppingCart function when the page loads
});
