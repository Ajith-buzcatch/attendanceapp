// polar chart js
// Fetching data from Django context variables
const weeklyAttendance = {{ weekly_attendance }};
const monthlyAttendance = {{ monthly_attendance }};
const yearlyAttendance = {{ yearly_attendance }};

var ctx = document.getElementById('myPolarChart').getContext('2d');
var myPolarChart = new Chart(ctx, {
    type: 'polarArea',
    data: {
        labels: ['Week', 'Month', 'Year'],
        datasets: [{
            label: 'Attendance report',
            data: [weeklyAttendance, monthlyAttendance, yearlyAttendance],
            backgroundColor: [
                'rgb(75, 192, 192)',
                'rgb(255, 205, 86)',
                'rgb(201, 203, 207)'
            ]
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'Attendance'
            }
        }
    }
});


// checkin , checkout, break buttons js

let countdownInterval;
let totalSeconds;
let breakSeconds = 0;
let breakStart = null;

function startCountdown() {
    countdownInterval = setInterval(function() {
        if (totalSeconds <= 0) {
            clearInterval(countdownInterval);
            return;
        }
        totalSeconds--;

        let hours = Math.floor(totalSeconds / 3600);
        let minutes = Math.floor((totalSeconds % 3600) / 60);
        let seconds = totalSeconds % 60;

        document.getElementById('hours').textContent = String(hours).padStart(2, '0');
        document.getElementById('minutes').textContent = String(minutes).padStart(2, '0');
        document.getElementById('seconds').textContent = String(seconds).padStart(2, '0');

        localStorage.setItem('totalSeconds', totalSeconds);
        localStorage.setItem('startTime', Date.now());
    }, 1000);
}

function stopCountdown() {
    clearInterval(countdownInterval);
    totalSeconds = 9 * 60 * 60; // Reset to 9 hours
    document.getElementById('hours').textContent = '09';
    document.getElementById('minutes').textContent = '00';
    document.getElementById('seconds').textContent = '00';
    localStorage.removeItem('totalSeconds');
    localStorage.removeItem('startTime');
    localStorage.removeItem('breakSeconds');
}

    function clearLocalStorage() {
    localStorage.removeItem('totalSeconds');
    localStorage.removeItem('startTime');
    localStorage.removeItem('breakSeconds');
    localStorage.removeItem('breakStart');
    localStorage.removeItem('breakActive');
    localStorage.removeItem('currentBreakType');
}

document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM loaded');
    resumeCountdown();

    const isNewUser = {{ is_new_user|yesno:"true,false" }};
    console.log('Is new user:', isNewUser);

    if (isNewUser) {
        
        document.getElementById('checkin-button').style.display = 'block';
        document.getElementById('break-buttons').style.display = 'none';
        
    }
});

function handleCheckIn() {
    getLocationAndSubmit('checkin', 'attendance-form', function(success) {
        if (success) {
            totalSeconds = 9 * 60 * 60; // 9 hours in seconds
            saveCountdownState();
            startCountdown();
            
            document.getElementById('checkin-button').style.display = 'none';
            document.getElementById('break-buttons').style.display = 'flex';
            document.getElementById('break-hours').style.display = 'block';
            
        }
    });
}

function showCheckoutAndBreakButtons() {
    document.getElementById('checkin-button').style.display = 'none';
    document.getElementById('checkout-button').style.display = 'block';
    document.getElementById('break-buttons').style.display = 'flex';
    document.getElementById('break-hours').style.display = 'block';
}

function getLocationAndSubmit(action, formId, callback) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            var latitude = position.coords.latitude;
            var longitude = position.coords.longitude;
            
            document.querySelectorAll('input[name="latitude"]').forEach(function(input) {
                input.value = latitude;
            });
            document.querySelectorAll('input[name="longitude"]').forEach(function(input) {
                input.value = longitude;
            });
            
            document.querySelector(`#${formId} input[name="action"]`).value = action;
            document.getElementById(formId).submit();
            
            if (callback) {
                callback(true);
            }
        }, function(error) {
            if (error.code === error.PERMISSION_DENIED) {
                alert('Please Enable Location');
            } else {
                alert('Error fetching location: ' + error.message);
            }
            
            if (callback) {
                callback(false);
            }
        });
    } else {
        alert('Geolocation is not supported by this browser.');
        
        if (callback) {
            callback(false);
        }
    }
}


// document.addEventListener('DOMContentLoaded', resumeCountdown);


function validateForgotCheckinForm() {
    var startTime = document.getElementById('start-time').value;
    var reason = document.getElementById('reason').value;

    if (!startTime || !reason) {
        alert('Please fill out all required fields.');
        return false;
    }
    return true;
}

function submitForgotCheckin() {
    if (validateForgotCheckinForm()) {
        getLocationAndSubmit('forgot_checkin', 'forgot-checkin-form');

        // Start the countdown after submitting forgot check-in
        totalSeconds = 9 * 60 * 60; // 9 hours in seconds
        saveCountdownState();
        startCountdown();
        toggleButtons(true);
    }
}



function confirmCheckout() {
    $('#checkoutModal').modal('show');

    document.getElementById('confirm-checkout').addEventListener('click', function() {
        getLocationAndSubmit('checkout', 'attendance-form', function(success) {
            if (success) {
                stopCountdown();
                $('#checkoutModal').modal('hide');
                
                //document.getElementById('checkin-button').style.display = 'block';
                //document.getElementById('break-buttons').style.display = 'none';
                //document.getElementById('break-hours').style.display = 'none';
            }
        });
    }, { once: true });
}

function handleBreak(type) {
    const teaBreakButton = document.getElementById('tea-break-button');
    const lunchBreakButton = document.getElementById('lunch-break-button');
    const checkoutButton = document.getElementById('checkout-button');

    if (breakStart) {
        breakSeconds += Math.floor((Date.now() - breakStart) / 1000);
        breakStart = null;
        updateBreakTime();

        if (type === 'tea') {
            teaBreakButton.innerHTML = '<ion-icon name="cafe-outline" class="align-left"></ion-icon><span class="bold">Tea Break</span>';
        } else if (type === 'lunch') {
            lunchBreakButton.innerHTML = '<ion-icon name="restaurant-outline" class="align-left"></ion-icon><span class="bold">Lunch Break</span>';
        }

        teaBreakButton.disabled = false;
        lunchBreakButton.disabled = false;
        checkoutButton.disabled = false;
        breakActive = false;
        currentBreakType = null;
    } else {
        breakStart = Date.now();
        if (type === 'tea') {
            teaBreakButton.innerHTML = '<ion-icon name="cafe-outline" class="align-left"></ion-icon><span class="bold">End Tea Break</span>';
            lunchBreakButton.disabled = true;
        } else if (type === 'lunch') {
            lunchBreakButton.innerHTML = '<ion-icon name="restaurant-outline" class="align-left"></ion-icon><span class="bold">End Lunch Break</span>';
            teaBreakButton.disabled = true;
        }
        checkoutButton.disabled = true;
        breakActive = true;
        currentBreakType = type;
    }

    localStorage.setItem('breakSeconds', breakSeconds);
    localStorage.setItem('breakStart', breakStart);
    localStorage.setItem('breakActive', breakActive);
    localStorage.setItem('currentBreakType', currentBreakType);

    
}

function updateBreakTime() {
    let hours = Math.floor(breakSeconds / 3600);
    let minutes = Math.floor((breakSeconds % 3600) / 60);
    let seconds = breakSeconds % 60;
    document.getElementById('break-time').textContent = 
        String(hours).padStart(2, '0') + ':' + 
        String(minutes).padStart(2, '0') + ':' + 
        String(seconds).padStart(2, '0');
}

function resumeCountdown() {
    let storedSeconds = localStorage.getItem('totalSeconds');
    let startTime = localStorage.getItem('startTime');
    breakSeconds = parseInt(localStorage.getItem('breakSeconds')) || 0;
    breakStart = parseInt(localStorage.getItem('breakStart')) || null;
    breakActive = localStorage.getItem('breakActive') === 'true';
    currentBreakType = localStorage.getItem('currentBreakType');

    if (storedSeconds && startTime) {
        let elapsed = Math.floor((Date.now() - startTime) / 1000);
        totalSeconds = storedSeconds - elapsed;

        if (totalSeconds > 0) {
            startCountdown();
            showCheckoutAndBreakButtons();
            //document.getElementById('checkin-button').style.display = 'none';
            //document.getElementById('break-buttons').style.display = 'flex';
            //document.getElementById('break-hours').style.display = 'block';
        } else {
            stopCountdown();
        }
    }

    const teaBreakButton = document.getElementById('tea-break-button');
    const lunchBreakButton = document.getElementById('lunch-break-button');
    const checkoutButton = document.getElementById('checkout-button');

    if (breakActive) {
        if (currentBreakType === 'tea') {
            teaBreakButton.innerHTML = '<ion-icon name="cafe-outline" class="align-left"></ion-icon><span class="bold">End Tea Break</span>';
            lunchBreakButton.disabled = true;
        } else if (currentBreakType === 'lunch') {
            lunchBreakButton.innerHTML = '<ion-icon name="restaurant-outline" class="align-left"></ion-icon><span class="bold">End Lunch Break</span>';
            teaBreakButton.disabled = true;
        }
        checkoutButton.disabled = true;
    }
    updateBreakTime();
}

function saveCountdownState() {
    localStorage.setItem('totalSeconds', totalSeconds);
    localStorage.setItem('startTime', Date.now());
    localStorage.setItem('breakSeconds', breakSeconds);
    localStorage.setItem('breakStart', breakStart);
    localStorage.setItem('breakActive', breakActive);
    localStorage.setItem('currentBreakType', currentBreakType);
}
