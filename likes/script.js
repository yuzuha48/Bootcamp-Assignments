function increaseLike(id) {
    var likeElement = document.querySelector(id);
    var like = parseInt(likeElement.innerText);
    likeElement.innerText = like + 1 + " like(s)";
}