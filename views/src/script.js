"use strict";

const add_input_enter_listener = () => {
  document.getElementById("array-input").addEventListener("keyup", (event) => {
    if (event.key === "Enter") {
      create_array();
    }
  });
};

const ensure_only_numbers = (array) => {
  if (array.length === 1 && array[0] === "") return [];
  return array.filter((element) => !isNaN(element));
};

const create_array_element = (father, element, index) => {
  const new_element = document.createElement("li");
  new_element.textContent = element;
  new_element.id = index;
  father.appendChild(new_element);
};

const create_array = () => {
  const input = document.getElementById("array-input");
  const array = ensure_only_numbers(input.value.split(","));
  const father = document.getElementById("array");
  father.innerHTML = "";

  father.array = array;
  array.forEach((element, index) => {
    create_array_element(father, element, index);
  });
};

const ordenate_array_elements = (steps) => {
  const array = document.getElementById("array");
  let delay = 0;

  steps.forEach((step) => {
    setTimeout(() => {
      if (step["i"] < array.children.length) {
        document.getElementById(step["i"]).classList.add("current");
        Array.from(array.children).forEach((element) => {
          if (element.id != step["i"]) element.classList.remove("current");
          for (let key in step) {
            if (key !== "i") {
              if (element.id == key.replace("_", "")) {
                console.log(
                  "step[key]",
                  step[key],
                  "\nkey",
                  key,
                  "\nelement.id",
                  element.id,
                  "\nstep",
                  step,
                );
                element.textContent = step[key];
              }
            }
          }
        });
      } else {
        Array.from(array.children).forEach((element) => {
          element.classList.remove("current");
        });
      }
    }, delay);
    delay += 1000;
  });
};

const sort_array = async () => {
  const array = document.getElementById("array").array;

  let sort_request = await fetch("/sort", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ array: array }),
  })
    .then((response) => response.json())
    .then((data) => {
      return data;
    })
    .catch((error) => console.error("Error:", error));

  ordenate_array_elements(sort_request);
};

const reset = () => {
  document.getElementById("array-input").value = "";
  let array = document.getElementById("array");
  array.innerHTML = "";
  array.array = "";
};
