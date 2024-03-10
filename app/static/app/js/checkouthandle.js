function submitFormData() {
    // var paypalBtn = document.getElementById('form-button-hi')
    // paypalBtn.addEventListener('click', function() {
    //     // var username = document.getElementById('checkout-username').value;
    //     // var email = document.getElementById('checkout-email').value;
    //     var address = document.getElementById('checkout-address').value;
    //     var city = document.getElementById('checkout-city').value;
    //     var state = document.getElementById('checkout-state').value;
    //     var phone = document.getElementById('checkout-phone').value;
    
    //     console.log(address)
    
    //     fetch('/update_checkout/', {
    //         method: 'POST',
    //         headers: {
    //             'Content-Type': 'application/json',
    //             'X-CSRFToken': csrftoken
    //         },
    //         body: JSON.stringify({
    //             // 'username': username,
    //             // 'email': email,
    //             'address': address,
    //             'city': city,
    //             'state': state,
    //             'phone': phone
    //         })
    //     })
    //     .then(response => response.json())
    //     .then(data => {
    //         console.log(data);
    //         location.reload();
    //     })
    //     .catch(error => {
    //         console.error('Error', error);
    //     })
    // })
    var address = document.getElementById('checkout-address').value;
    var city = document.getElementById('checkout-city').value;
    var state = document.getElementById('checkout-state').value;
    var phone = document.getElementById('checkout-phone').value;

    console.log(address)

    fetch('/update_checkout/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            // 'username': username,
            // 'email': email,
            'address': address,
            'city': city,
            'state': state,
            'phone': phone
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        location.reload();
    })
    .catch(error => {
        console.error('Error', error);
    })
}