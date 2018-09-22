import { getTrials } from "./experiment.js";

$(document).ready(function(){
    let workerId = $.urlParam('workerId') || 'unknown';
    let assignmentId = undefined;
    let hitId = undefined;
    getTrials(workerId, assignmentId, hitId);    
});
