// Frontend adapter for the TrustCheck Intelligent Contract.
// Replace CONTRACT_ADDRESS and RPC_URL with your deployed GenLayer values.
const CONTRACT_ADDRESS = "YOUR_TRUSTCHECK_CONTRACT_ADDRESS";
const RPC_URL = "YOUR_GENLAYER_RPC_URL";

const $ = (id) => document.getElementById(id);

$("submit").addEventListener("click", async () => {
  const claim = $("claim").value.trim();
  const source = $("source").value.trim();
  if (!claim || !source) {
    $("status").textContent = "Enter both a claim and source URL.";
    return;
  }

  $("status").textContent = "Preparing GenLayer transaction…";
  // Integration point: connect a GenLayer-compatible wallet/provider here,
  // call submit_claim(claim, source), wait for confirmation, then call evaluate
  // and get_result(). The UI intentionally exposes the complete lifecycle.
  if (CONTRACT_ADDRESS.startsWith("YOUR_")) {
    $("status").textContent = "Demo UI ready — configure the deployed contract and RPC to send a live transaction.";
    $("result").hidden = false;
    $("result").textContent = JSON.stringify({ claim, source, result: "PENDING" }, null, 2);
    return;
  }

  $("status").textContent = "Live integration configured. Connect your GenLayer provider to continue.";
});
