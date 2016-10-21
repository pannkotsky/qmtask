function displayQuantity () {
    var select = document.getElementById('good');
    var pricingUnit = select.options[select.selectedIndex].getAttribute("data-good-pu");
    var style = pricingUnit !== '1' ? 'block' : 'none';
    document.getElementById('quantity').style.display = style;
}

document.addEventListener("DOMContentLoaded", displayQuantity);
document.getElementById('good').addEventListener('change', displayQuantity);
