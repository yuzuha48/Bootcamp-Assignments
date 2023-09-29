// $(document).ready(function () {
//     $('#createUserForm').on('submit', function (e) {
//         e.preventDefault();
//         const formData = $(this).serialize();
    
//         $.ajax({
//             type: 'POST', 
//             url: '/shows/new',
//             data: formData, 
//             success: function (response) {
//                 if (response.error) {
//                     // $('#errorMessage').empty();
//                     $('#errorMessage').text(response.error);
//                 }
//             },
//             error: function (xhr, errmsg, err) {
//                 console.log(xhr.status + ": " + xhr.responseText);
//             }
//         })
//     })
// })

// $(document).ready(function () {
//     $('#updateUserForm').on('submit', function (e) {
//         e.preventDefault();
//         const formData = $(this).serialize();
//         const showId = $('#show_id').val();
    
//         $.ajax({
//             type: 'POST', 
//             url: `/shows/$(showID)/edit`,
//             data: formData, 
//             success: function (response) {
//                 if (response.error) {
//                     // $('#errorMessage').empty();
//                     $('#errorMessage').text(response.error);
//                 }
//             },
//             error: function (xhr, errmsg, err) {
//                 console.log(xhr.status + ": " + xhr.responseText);
//             }
//         })
//     })
// })