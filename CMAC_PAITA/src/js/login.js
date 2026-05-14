const form =
document.getElementById(
    "loginForm"
);

form.addEventListener(
    "submit",
    () => {

        document.getElementById(
            "loadingScreen"
        ).style.display = "flex";

    }
);