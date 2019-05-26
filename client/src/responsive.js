if (window.innerWidth < 500) {
    document.getElementById('locationInput').style.width = ((window.innerWidth / 6) * 3) + "";
    document.getElementById('setLocation').style.width = ((window.innerWidth / 6) * 1.5) + "";
    document.getElementById('search').classList.add('mobile')
} else {
    document.getElementById('search').classList.add('desktop')
}