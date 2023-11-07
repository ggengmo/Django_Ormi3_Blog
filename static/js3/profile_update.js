let profileImageInput = document.querySelector('#id_profile_image');
let profileImagePreview = document.querySelector('#profileImagePreview');

profileImageInput.addEventListener('change', function (e) {
    let file = e.target.files[0];
    let reader = new FileReader();
    
    reader.onload = function (e) {
        profileImagePreview.src = e.target.result;
    };
    
    reader.readAsDataURL(file);
});