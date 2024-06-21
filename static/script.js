document.getElementById('herbForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const symptom = document.getElementById('symptom').value;
    const herb_id = document.getElementById('herb_id').value;

    fetch('/get_medicine', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symptom, herb_id })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('formulation').textContent = 'Medicine Formulation: ' + data.formulation;
        document.getElementById('herb_name').textContent = 'Herb Name: ' + data.herb_name;
    })
    .catch(error => console.error('Error:', error));
});
