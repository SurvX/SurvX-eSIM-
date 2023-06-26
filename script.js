onst RippleAPI = require('ripple-lib').RippleAPI;

// Connect to the XRP Ledger
const api = new RippleAPI({
  server: 'wss://s.altnet.rippletest.net:51233' // Testnet server
});
api.connect().then(() => {
  console.log('Connected to the XRP Ledger');

  // Get account balance
  const accountAddress = 'your_account_address';
  api.getAccountInfo(accountAddress).then(info => {
    console.log('Account Balance:', info.xrpBalance);
  }).catch(error => {
    console.error('Error getting account balance:', error);
  });

  // Send payment
  const senderSecret = 'your_sender_secret';
  const recipientAddress = 'recipient_account_address';
  const paymentAmount = '10'; // Amount in XRP

  const payment = {
    source: {
      address: accountAddress,
      maxAmount: {
        value: paymentAmount,
        currency: 'XRP'
      }
    },
    destination: {
      address: recipientAddress,
      amount: {
        value: paymentAmount,
        currency: 'XRP'
      }
    }
  };

  api.preparePayment(accountAddress, payment, {
    maxLedgerVersionOffset: 5
  }).then(prepared => {
    const { signedTransaction } = api.sign(prepared.txJSON, senderSecret);
    return api.submit(signedTransaction);
  }).then(result => {
    console.log('Payment sent:', result);
  }).catch(error => {
    console.error('Error sending payment:', error);
  }).finally
