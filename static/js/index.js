console.log("Hello World!");
let sectionTitle = document.getElementsByClassName("section-title")[0];
let mainSection = document.getElementsByClassName("main-section")[0];

let sectionTitleHeight = sectionTitle.offsetHeight;
let sectionTitleWidth = sectionTitle.offsetWidth;
mainSection.style.paddingTop = sectionTitleHeight + "px";
mainSection.offsetWidth = sectionTitleWidth + "px";