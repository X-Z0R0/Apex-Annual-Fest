window.addEventListener('error', function (event) {
    // Check if the error message contains the specific string
    if (event.message && event.message.includes('Failed to load resource: net::ERR_INTERNET_DISCONNECTED')) {
      // Show alert for internet connection issue
      alert('Internet connection is not available.');
    }
  });

let orderIDFromUrl = null;
let amountFromUrl = null;
// let loader = document.getElementById("loader");
document.addEventListener("DOMContentLoaded", function () {
    updateButtonVisibility();  // Call the function here
    document.querySelectorAll('.pay-button').forEach(function (button) {
        button.addEventListener('click', function (e) {
            loader.style.display = 'block';
            e.preventDefault();
            var teamID = this.getAttribute('data-teamid');
            var action = this.getAttribute('data-action');
            $.ajax({
                type: 'POST',
                url: '/Spoorti/SpoortiDashboard/',
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
                    updateButtonVisibility(); 
                },
                error: function (error) {
                    // console.log('Error sending data to the server:', error);
                    // Display the error in an alert box
                    loader.style.display = 'none';
                    alert('An error occurred.(check internet connection)',error);
                },
                complete: function () {
                 // Hide loader after AJAX request is complete
                    loader.style.display = 'none';
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
            name: "Apexian",
            description: "Test Transaction",
            image: "https://th.bing.com/th/id/OIP.8ldltV-HqKgFQCfOFXV44AAAAA?rs=1&pid=ImgDetMain",
            order_id: orderIDFromUrl,
            handler: function (response) {
                $.ajax({
                    type: 'POST',
                    url: '/Spoorti/SpoortiDashboard/',
                    data: {
                        'action': 'paymentDetail',
                        'razorpay_payment_id': response.razorpay_payment_id,
                        'razorpay_order_id': response.razorpay_order_id,
                        'razorpay_signature': response.razorpay_signature,
                        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
                    },
                    success: function (data) {
                        alert('success');
                        window.location.href = data.redirect_url;
                    },
                    error: function (error) {
                        //console.error('Payment error:', error);
                        // alert('Payment failed. Please try again later.');
                        window.location.href = data.redirect_url; 
                    },
                    // complete:function(){
                    //     console.log("completed")
                    //     window.location.href = 'http://127.0.0.1:8000/Spoorti/SpoortiDashboard/';
                    // }
                });
            },
            theme: {
                color: "#ff471a",
            },
        };
        var rzp1 = new Razorpay(options);
        rzp1.on("payment.failed", function (response) {
            // alert(response.error.code);
            // alert(response.error.description);
            // alert(response.error.source);
            // alert(response.error.step);
            // alert(response.error.reason);
            // alert(response.error.metadata.order_id);
            // alert(response.error.metadata.payment_id);
            // Log detailed error information for debugging on the server side
            //console.error('Payment failed:', response);
            // Display a generic error message to the user
                alert('Payment failed. Please try again later.');
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
        if (button !== event.target) {
            button.style.display = 'none';
        } else {
            button.disabled = true;
            // button.style.backgroundColor = 'black';
        }
    });
}

function enableOtherPayButtons() {
    document.querySelectorAll('.pay-button').forEach(function (button) {
        // button.disabled = false;
        // button.style.backgroundColor = "#ff471a"; 
        button.style.display = 'block';
        button.disabled = false;
        // button.style.backgroundColor = '';
    });
}