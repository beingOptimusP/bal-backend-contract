const Web3 = require("web3")
const abi = require("./abi.json")
// console.log(abi)


var w3 = new Web3('https://eth-goerli.g.alchemy.com/v2/3Cfhb0ZB3R-Lr_9FIpnI4mPouvQkUr0f');
// w3 = Web3(Web3.HTTPProvider('https://eth-goerli.g.alchemy.com/v2/3Cfhb0ZB3R-Lr_9FIpnI4mPouvQkUr0f'))


privateKey = "0d845b90a56f9e4709ba682e87be6a58417b27108c14ddeb7ab8c42251803559"

contract_addy = "0x771500444863dB465bb5AFAA95e1654Ae15f6Acf"

addy = "0xBaFa7Da92715a1b06397bF26E6e335599769b412"

const contract  = new w3.eth.Contract(abi,contract_addy)

const fun = async () =>{
    // var bal = await w3.eth.getBalance(addy)
    // console.log(bal)
    // const tx = {
    //     // this could be provider.addresses[0] if it exists
    //     from: addy, 
    //     // target address, this could be a smart contract address
    //     to: contract_addy, 
    //     // optional if you want to specify the gas limit 
    //     gas: 100000,
    //     // this encodes the ABI of the method and the arguements
    //     data: contract.methods.emitEvent(1,2,3).encodeABI() 
    //   };
    // // console.log(events.events)
    // const signPromise = w3.eth.accounts.signTransaction(tx, privateKey);
    // signPromise.then((signedTx) => {
    //     // raw transaction string may be available in .raw or 
    //     // .rawTransaction depending on which signTransaction
    //     // function was called
    //     const sentTx = w3.eth.sendSignedTransaction(signedTx.raw || signedTx.rawTransaction);
    //     sentTx.on("receipt", receipt => {
    //       // do something when receipt comes back
    //       console.log(receipt.events)
    //     });
    //     sentTx.on("error", err => {
    //       // do something on transaction error
    //     });
    //   }).catch((err) => {
    //     // do something when promise fails
    //   });
    const result = await contract.getPastEvents(
        'logs',
        {fromBlock:0},
    )

    console.log(result)
}

fun()