document.getElementById('executeButton').addEventListener('click', () => {
  const ipAddress = document.getElementById('ipAddressInput').value;
  chrome.runtime.sendNativeMessage('com.example.batexecutor', { ip_address: ipAddress }, (response) => {
    if (chrome.runtime.lastError) {
      console.error('Error: ' + chrome.runtime.lastError.message);
      return;
    }
    if (response && response.response) {
      alert(response.response);
    } else if (response && response.error) {
      alert('Error: ' + response.error);
    } else {
      alert('Failed to execute .bat file.');
    }
  });
});
