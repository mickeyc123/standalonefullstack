function removeItem(index) {
    var orders = JSON.parse(localStorage.getItem('cart'));

    // Remove the item from the orders array
    orders.splice(index, 1);

    // Save the updated orders array back to localStorage
    localStorage.setItem('cart', JSON.stringify(orders));

    // Call shoppingCart again to update the display
    shoppingCart();
}
