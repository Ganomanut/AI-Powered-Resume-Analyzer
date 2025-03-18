
document.getElementById("submit-btn").addEventListener("click", function() {
    let candidateStatus = document.getElementById("candidate-status").value;
    let jobId = document.getElementById("job-id").value;
    let role = document.getElementById("role").value;
    let submissionDate = document.getElementById("submission-date").value;
    let communicationLogs = document.getElementById("communication-logs").value;
    
    if (!jobId || !role || !submissionDate) {
        alert("Please fill out all required fields.");
        return;
    }
    
    let candidateData = {
        status: candidateStatus,
        jobId: jobId,
        role: role,
        submissionDate: submissionDate,
        communicationLogs: communicationLogs
    };
    console.log("Candidate Data Saved:", candidateData);
    alert("Candidate information saved successfully!");
});