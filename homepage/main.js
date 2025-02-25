async function rickroll(){
    var video = document.createElement("video");
    video.load();
    video.src = "norickroll.mp4";
    video.style.display = "block";
    video.style.position = "fixed";
    video.style.top = "0";
    video.style.left = "0";
    video.style.width = "100%";
    video.style.height = "auto";
    video.style.right = "0";
    video.style.bottom = "0";
    await video.play();
    document.open();
    document.appendChild(video);
    document.close();
}

document.getElementById("roll").addEventListener("click",rickroll);
