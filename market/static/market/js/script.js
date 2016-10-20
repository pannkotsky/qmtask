document.getElementById('good').addEventListener('change', function () {
    var style = this.value == '3' ? 'block' : 'none';
    document.getElementById('quantity').style.display = style;
});
