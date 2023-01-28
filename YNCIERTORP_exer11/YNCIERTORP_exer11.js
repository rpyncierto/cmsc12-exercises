// initialization part for global variables
var restriction = document.getElementsByName('restriction')
var foods = document.getElementsByName('food')
var carbs = document.getElementsByClassName('carbs')
var veggies = document.getElementsByClassName('veggies')
var meats = document.getElementsByClassName('protein')
var form = document.querySelector('#planner')

// Disables meat options if vegetarian is selected, and enables them if vegetarian is not selected, via the target event property, which returns the element on which the event occurred.
for (var i = 0; i < restriction.length; i++) {
    restriction[i].addEventListener('change', function (event) {
        for (var i = 0; i < meats.length - 1; i++) {
            if (event.target.value === 'vegetarian') {
                meats[i].disabled = true
                meats[i].checked = false
            } else {
                meats[i].disabled = false
            }
        }
    }
    )
}

form.addEventListener('submit', function (e) {
    e.preventDefault()

    // initialization part for local variables
    var foodsCount = 0
    var carbsCount = 0
    var veggiesCount = 0
    var totalCalories = 0
    var plan = ''

    // obtains the user-selected dietary plan
    for (var i = 0; i < restriction.length; i++) {
        if (restriction[i].checked) {
            plan = restriction[i].value
        }
    }

    // obtains the total number of calories in the foods selected by the user
    for (var i = 0; i < foods.length; i++) {
        if (foods[i].checked) {
            foodsCount++
            totalCalories += parseInt(foods[i].value)
        }
    }

    // counts the number of foods selected by the user under the carbohydrate classification
    for (var i = 0; i < carbs.length; i++) {
        if (carbs[i].checked) {
            carbsCount++
        }
    }

    // counts the number of foods selected by the user under the veggies classification
    for (var i = 0; i < veggies.length; i++) {
        if (veggies[i].checked) {
            veggiesCount++
        }
    }

    // If the user's inputs satisfy a criterion, the associated alert is displayed.
    if (foodsCount < 2) {
        alert('At least 2 food items should be selected.')
    } else {
        if (plan === 'lowcarb' && carbsCount > 2) {
            alert('More than 2 carbohydrate options are selected.')
        } else if (veggiesCount < 2) {
            alert('At least 2 veggies are recommended for a healthy meal' + '\nTotal calories: ' + totalCalories);
        } else if (totalCalories > 750) {
            alert('Total calories: ' + totalCalories + "\nYou shouldn't be eating this much.")
        } else if (totalCalories < 400) {
            alert('Total calories: ' + totalCalories + '\nYou are eating too little.')
        } else {
            alert(`Total calories: ` + totalCalories)
        }
    }
}
)
