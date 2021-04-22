
// this is called when the backend sends any message
function runCommand(cmd) {
    if (cmd.function == 'play') {
        play(cmd.note);
    }
}

const synth = new Tone.Synth().toDestination();

function play(note) {
    synth.triggerAttackRelease(note, "8n")
}