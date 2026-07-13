// ================= DOM ELEMENTS =================

const uploadBox = document.getElementById("uploadBox");
const videoInput = document.getElementById("videoInput");
const uploadStatus = document.getElementById("uploadStatus");
const healthStatus = document.getElementById("healthStatus");

const questionInput = document.getElementById("questionInput");
const askButton = document.getElementById("askButton");

const answerSection = document.getElementById("answerSection");
const loadingSpinner = document.getElementById("loadingSpinner");
const answerContent = document.getElementById("answerContent");


// ================= CONFIG =================

const API_URL = "http://127.0.0.1:5000";


// ================= STATE =================

let videoUploaded = false;


// ================= BACKEND CHECK =================

async function checkBackendHealth() {

    try {

        const response = await fetch(`${API_URL}/`);

        const text = await response.text();

        console.log("Backend:", text);

        if (healthStatus) {
            healthStatus.innerText = "🟢 Backend Connected";
            healthStatus.style.color = "green";
        }

    } catch(error) {

        console.error(error);

        if (healthStatus) {
            healthStatus.innerText = "🔴 Backend Not Connected";
            healthStatus.style.color = "red";
        }
    }
}


checkBackendHealth();



// ================= UPLOAD CLICK =================

if(uploadBox){

uploadBox.addEventListener("click",()=>{

    videoInput.click();

});

}



// ================= FILE SELECT =================

videoInput.addEventListener("change",()=>{

    const file = videoInput.files[0];

    if(file){

        uploadVideo(file);

    }

});



// ================= DRAG DROP =================


uploadBox.addEventListener("dragover",(e)=>{

    e.preventDefault();

    uploadBox.style.opacity="0.7";

});


uploadBox.addEventListener("dragleave",()=>{

    uploadBox.style.opacity="1";

});


uploadBox.addEventListener("drop",(e)=>{

    e.preventDefault();

    uploadBox.style.opacity="1";


    const file=e.dataTransfer.files[0];


    if(file){

        uploadVideo(file);

    }

});



// ================= VIDEO UPLOAD =================


async function uploadVideo(file){


    if(!file.type.startsWith("video/")){

        uploadStatus.innerText="❌ Please upload a video file";

        return;

    }


    const formData=new FormData();


    formData.append("video",file);



    uploadStatus.innerText="⏳ Uploading and processing video...";



    try{


        const response=await fetch(
            `${API_URL}/upload`,
            {
                method:"POST",
                body:formData
            }
        );



        const data=await response.json();


        console.log("UPLOAD RESPONSE:",data);



        if(!response.ok){

            throw new Error(data.error);

        }



        uploadStatus.innerText=
        "✅ Video processed successfully";


        uploadStatus.style.color="green";



        videoUploaded=true;



        // enable question box

        questionInput.disabled=false;

        askButton.disabled=false;


        questionInput.removeAttribute("disabled");

        askButton.removeAttribute("disabled");



        console.log(
            "Question enabled"
        );



    }

    catch(error){


        console.error(
            "UPLOAD ERROR:",
            error
        );


        uploadStatus.innerText=
        "❌ Upload failed : "+error.message;


        uploadStatus.style.color="red";


        videoUploaded=false;


    }


}





// ================= ASK QUESTION =================


askButton.addEventListener(
"click",
askQuestion
);



questionInput.addEventListener(
"keypress",
(e)=>{

    if(e.key==="Enter"){

        askQuestion();

    }

});





async function askQuestion(){


    const query=
    questionInput.value.trim();



    if(!query){

        alert("Enter a question");

        return;

    }



    if(!videoUploaded){

        alert("Upload video first");

        return;

    }




    answerSection.style.display="block";


    loadingSpinner.style.display="block";


    answerContent.innerHTML="";




    try{


        console.log(
            "Sending question:",
            query
        );



        const response=
        await fetch(
            `${API_URL}/ask`,
            {

                method:"POST",

                headers:{

                    "Content-Type":
                    "application/json"

                },


                body:
                JSON.stringify(
                    {
                        query:query
                    }
                )

            }
        );




        const data=
        await response.json();



        console.log(
            "ANSWER:",
            data
        );



        if(!response.ok){

            throw new Error(
                data.error
            );

        }




        loadingSpinner.style.display="none";



        answerContent.innerText=
        data.answer;



    }


    catch(error){



        console.error(
            error
        );



        loadingSpinner.style.display="none";



        answerContent.innerHTML=
        `
        <p style="color:red">
        ❌ ${error.message}
        </p>
        `;


    }



}