const pins =
document.querySelectorAll(
    ".pin"
);

// ======================
// AUTO NEXT
// ======================

pins.forEach(

    (input, index) => {

        input.addEventListener(

            "input",

            () => {

                if (

                    input.value.length === 1 &&
                    index < pins.length - 1

                ) {

                    pins[index + 1].focus();

                }

            }

        );

    }

);

// ======================
// FORM
// ======================

const form =
document.getElementById(
    "registerForm"
);

const hiddenPin =
document.getElementById(
    "hiddenPin"
);

form.addEventListener(

    "submit",

    (e) => {

        // ======================
        // PASSWORDS
        // ======================

        const password =
        document.querySelector(
            'input[name="password"]'
        ).value;

        const confirmPassword =
        document.querySelector(
            'input[name="confirm_password"]'
        ).value;

        if (

            password !== confirmPassword

        ) {

            e.preventDefault();

            alert(
                "Las contraseñas no coinciden"
            );

            return;

        }

        // ======================
        // PIN
        // ======================

        let finalPin = "";

        pins.forEach(

            (pin) => {

                finalPin += pin.value;

            }

        );

        hiddenPin.value = finalPin;

        // ======================
        // LOADING
        // ======================

        document.getElementById(
            "loadingScreen"
        ).style.display = "flex";

    }

);