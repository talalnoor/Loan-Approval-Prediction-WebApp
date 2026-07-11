document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('loanForm');

    if (form) {
        form.addEventListener('submit', function (e) {
            let hasError = false;

            // Check every required field; flag empty ones visually
            const inputs = form.querySelectorAll('input[required], select[required]');
            inputs.forEach(function (input) {
                if (!input.value.trim()) {
                    input.classList.add('invalid');
                    hasError = true;
                } else {
                    input.classList.remove('invalid');
                }
            });

            if (hasError) {
                e.preventDefault();
                return;
            }

            // Show a loading state on the button while Flask processes the prediction
            const submitBtn = form.querySelector('.submit-btn');
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing Application...';
            submitBtn.disabled = true;
        });

        // Remove the red "invalid" highlight as soon as the user starts fixing a field
        form.querySelectorAll('input, select').forEach(function (field) {
            field.addEventListener('input', function () {
                field.classList.remove('invalid');
            });
        });
    }
});