document.addEventListener('DOMContentLoaded', function() {
    // var paypalBtn = document.getElementById('form-button-hi')
    // paypalBtn.addEventListener('click', function() {
    //     var username = document.getElementById('checkout-username').value;
    //     var email = document.getElementById('checkout-email').value;
    //     var address = document.getElementById('checkout-address').value;
    //     var city = document.getElementById('checkout-city').value;
    //     var state = document.getElementById('checkout-state').value;
    //     var phone = document.getElementById('checkout-phone').value;

    //     console.log('haha')

    //     // fetch('/update_checkout/', {
    //     //     method: 'POST',
    //     //     headers: {
    //     //         'Content-Type': 'application/json',
    //     //         'X-CSRFToken': csrftoken
    //     //     },
    //     //     body: JSON.stringify({
    //     //         'username': username,
    //     //         'email': email,
    //     //         'address': address,
    //     //         'city': city,
    //     //         'state': state,
    //     //         'phone': phone
    //     //     })
    //     // })
    //     // .then(response => response.json())
    //     // .then(data => {
    //     //     console.log(data);
    //     // })
    //     // .catch(error => {
    //     //     console.error('Error', error);
    //     // })
    // })
    var updateBtns = document.getElementsByClassName('update-cart')

    for (i = 0; i < updateBtns.length; i++) {
        updateBtns[i].addEventListener('click', function() {
            var productId = this.dataset.product
            var action = this.dataset.action
            console.log('productId', productId, 'action', action)
            console.log('user: ', user)
            if (user === "AnonymousUser") {
                console.log('user not logged')
            } else {
                updateUserOrder(productId, action)
            }
        })
    }

    function updateUserOrder(productId, action) {
        console.log('user logged in, success add')
        var url = '/update_item/'
        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrftoken
            },
            body: JSON.stringify({'productId':productId, 'action':action})

        })
        .then((response) => {
            return response.json()
        })
        .then((data) => {
            console.log('data', data)
            location.reload()
        })
    }
})