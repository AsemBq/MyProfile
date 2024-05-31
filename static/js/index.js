document.querySelector("li.AboutMe").addEventListener("click",()=>{
    document.querySelector(".countainer nav ul li.active").classList.remove("active")
    document.querySelector(".sections section.active").classList.remove("active")
    document.querySelector(".countainer nav ul li.AboutMe").classList.add('active')
    document.querySelector("section.AboutMe").classList.add('active')
    
  })
  
  document.querySelector("li.MySkilles").addEventListener("click",()=>{
    document.querySelector(".countainer nav ul li.active").classList.remove("active");
    document.querySelector(".sections section.active").classList.remove("active")
    document.querySelector(".countainer nav ul li.MySkilles").classList.add('active')
    document.querySelector('section.Tecnology').classList.add('active')
  })
  
  document.querySelector("li.MyProject").addEventListener("click",()=>{
    document.querySelector(".countainer nav ul li.active").classList.remove("active");
    document.querySelector(".sections section.active").classList.remove("active")
    document.querySelector(".countainer nav ul li.MyProject").classList.add('active')
    document.querySelector('section.MyProject').classList.add('active')
  })

  document.querySelector("#ContactMe").addEventListener("click",()=>{
    document.querySelector(".countainer nav ul li.active").classList.remove("active");
    document.querySelector(".sections section.active").classList.remove("active")
    document.querySelector("#ContactMe").classList.add('active')
    document.querySelector('section.ContactMe').classList.add('active')
  })



// for mobile 


document.querySelector("#About").addEventListener("click",()=>{
    document.querySelector("nav.mobile-nav ul li.active").classList.remove("active");
    document.querySelector("#About").classList.add('active');
    document.querySelector(".sections section.active").classList.remove("active");
    document.querySelector('section.AboutMe').classList.add('active');
})

document.querySelector("#Skilles").addEventListener("click",()=>{
    document.querySelector("nav.mobile-nav ul li.active").classList.remove("active");
    document.querySelector("#Skilles").classList.add('active');
    document.querySelector(".sections section.active").classList.remove("active");
    document.querySelector('section.Tecnology').classList.add('active');
})

document.querySelector("#projects").addEventListener("click",()=>{
    document.querySelector("nav.mobile-nav ul li.active").classList.remove("active");
    document.querySelector("#projects").classList.add('active');
    document.querySelector(".sections section.active").classList.remove("active");
    document.querySelector('section.MyProject').classList.add('active');
})

document.querySelector("#liContact").addEventListener("click",()=>{
  document.querySelector("nav.mobile-nav ul li.active").classList.remove("active");
  document.querySelector("#liContact").classList.add('active');
  document.querySelector(".sections section.active").classList.remove("active");
  document.querySelector('section.ContactMe').classList.add('active');
})
