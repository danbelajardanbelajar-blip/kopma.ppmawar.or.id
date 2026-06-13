function calculateSimulation() {
    const amountStr = document.getElementById('sim_amount').value;
    const amount = parseFloat(amountStr.replace(/[^0-9]/g, ''));
    const tenor = parseInt(document.getElementById('sim_tenor').value);
    
    const productSelect = document.getElementById('sim_product');
    const marginRate = parseFloat(productSelect.options[productSelect.selectedIndex].dataset.margin);
    
    if (isNaN(amount) || isNaN(tenor) || isNaN(marginRate)) return;
    
    const marginAmount = (amount * (marginRate / 100) * (tenor / 12));
    const totalPayment = amount + marginAmount;
    const monthlyPayment = totalPayment / tenor;
    
    document.getElementById('res_amount').innerText = formatRupiah(amount);
    document.getElementById('res_margin').innerText = formatRupiah(marginAmount);
    document.getElementById('res_total').innerText = formatRupiah(totalPayment);
    document.getElementById('res_monthly').innerText = formatRupiah(monthlyPayment);
    
    document.getElementById('simulation_result').style.display = 'block';
}

function formatRupiah(angka) {
    return new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', minimumFractionDigits: 0 }).format(angka);
}

document.addEventListener('DOMContentLoaded', function() {
    const simAmount = document.getElementById('sim_amount');
    if (simAmount) {
        simAmount.addEventListener('keyup', function(e) {
            let val = this.value.replace(/[^0-9]/g, '');
            if(val) {
                this.value = new Intl.NumberFormat('id-ID').format(val);
            }
        });
    }
});
