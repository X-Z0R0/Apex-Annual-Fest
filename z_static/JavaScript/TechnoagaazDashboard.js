let orderIDFromUrl = null;
let amountFromUrl = null;
document.addEventListener("DOMContentLoaded", function () {
    updateButtonVisibility();  // Call the function here
    document.querySelectorAll('.pay-button').forEach(function (button) {
        button.addEventListener('click', function (e) {
            e.preventDefault();
            var teamID = this.getAttribute('data-teamid');
            var action = this.getAttribute('data-action');
            $.ajax({
                type: 'POST',
                url: '/Technoagaaz/TechnoagaazDashboard/',
                data: {
                    'teamID': teamID,
                    'action': action,
                    'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                },
                success: function (data) {
                    console.log('Received data from the server:', data);
                    var urlParams = new URLSearchParams(data.redirect_url);
                    amountFromUrl = urlParams.get('amount');
                    orderIDFromUrl = urlParams.get('order_id');
                    alert(amountFromUrl)
                    alert(orderIDFromUrl)
                    updateButtonVisibility();
                },
                error: function (error) {
                    console.log('Error sending data to the server:', error);
                    loader.style.display = 'none';
                    alert('An error occurred.(check internet connection)',error);
                }
            });
        });
    });

    document.getElementById("rzp-button1").onclick = function (e) {
        this.disabled = true;
        var options = {
            key: "rzp_test_JlKOkCcJe3WrmP",
            amount: amountFromUrl,
            currency: "INR",
            name: "Acme Corp",
            description: "Test Transaction",
            image: "https://example.com/your_logo",
            order_id: orderIDFromUrl,
            handler: function (response) {
                $.ajax({
                    type: 'POST',
                    url: '/Technoagaaz/TechnoagaazDashboard/',
                    data: {
                        'action': 'paymentDetail',
                        'razorpay_payment_id': response.razorpay_payment_id,
                        'razorpay_order_id': response.razorpay_order_id,
                        'razorpay_signature': response.razorpay_signature,
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success: function (data) {
                        window.location.href = data.redirect_url;
                    },
                    error: function (error) {
                        window.location.href = data.redirect_url;
                    }
                });
            },
            theme: {
                color: "#3399cc",
            },
        };
        var rzp1 = new Razorpay(options);
        rzp1.on("payment.failed", function (response) {
            alert(response.error.code);
            alert(response.error.description);
            alert(response.error.source);
            alert(response.error.step);
            alert(response.error.reason);
            alert(response.error.metadata.order_id);
            alert(response.error.metadata.payment_id);
        });
        rzp1.open();
        e.preventDefault();
    };
});

function updateButtonVisibility() {
    var buttonElement = document.getElementById("rzp-button1");
    if (orderIDFromUrl === null) {
        buttonElement.style.display = "none";
        enableOtherPayButtons();
    } else {
        buttonElement.style.display = "block";
        disableOtherPayButtons(); 
    }
}

function disableOtherPayButtons() {
    document.querySelectorAll('.pay-button').forEach(function (button) {
        // button.disabled = true;
        // button.style.backgroundColor = "black";
        // console.log('disable')
        if (button !== event.target) {
            button.style.display = 'none';
        } else {
            button.disabled = true;
            button.style.backgroundColor = 'black';
        }
    });
}

function enableOtherPayButtons() {
    document.querySelectorAll('.pay-button').forEach(function (button) {
        // button.disabled = false;
        // button.style.backgroundColor = "#ff471a"; 
        button.style.display = 'block';
        button.disabled = false;
        button.style.backgroundColor = '#ff471a';
    });
}