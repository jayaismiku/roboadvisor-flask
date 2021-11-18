/* Fungsi formatRupiah */
function formatRupiah(angka, prefix) {
  var number_string = angka.replace(/[^,\d]/g, "").toString(),
    split = number_string.split(","),
    sisa = split[0].length % 3,
    rupiah = split[0].substr(0, sisa),
    ribuan = split[0].substr(sisa).match(/\d{3}/gi);

	if (ribuan) {
	  separator = sisa ? "." : "";
	  rupiah += separator + ribuan.join(".");
	}
	rupiah = split[1] != undefined ? rupiah + "," + split[1] : rupiah;
	return prefix == undefined ? rupiah : rupiah ? "Rp. " + rupiah : "";
}

var hargarumah = document.querySelector('#hargarumah');
hargarumah.addEventListener("keyup", function (e) {
  hargarumah.value = formatRupiah(this.value, "Rp. ");
});

var uangmuka = document.getElementById('uangmuka');
uangmuka.addEventListener("keyup", function (e) {
  uangmuka.value = formatRupiah(this.value, "Rp. ");
});

// $('#hargarumah').keyup(function () {
// 	alert(this.value);
// });

$(document).ready(function () {
	$('#batal').click(function(){

	})

	$("#alamatkota").change(function () {
		$.ajax({
			url: "/form/getKelurahan/" + this.value,
				success: function (result) {
				$("#div1").html(result);
			}
		});
	});

	$('#btnSignUp').click(function() {
		$.ajax({
			url: '/signUp',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response) {
				console.log(response);
			},
			error: function(error) {
				console.log(error);
			}
		});
	});
})


//Back Button
const backButton = document.querySelectorAll('[data-back-button]');
if (backButton.length) {
  backButton.forEach(el => el.addEventListener('click', e => {
    e.stopPropagation;
    e.preventDefault;
    window.history.go(-1);
  }));
}

//Back to Top
const backToTop = document.querySelectorAll('.back-to-top-icon, .back-to-top-badge, .back-to-top');
if (backToTop.length) {
  backToTop.forEach(el => el.addEventListener('click', e => {
    window.scrollTo({ top: 0, behavior: `smooth` })
  }));
}
