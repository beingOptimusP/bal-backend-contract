const Web3 = require("web3")
const abi = require("./abi.js")
// console.log(abi)


var w3 = new Web3('https://eth-goerli.g.alchemy.com/v2/3Cfhb0ZB3R-Lr_9FIpnI4mPouvQkUr0f');
// w3 = Web3(Web3.HTTPProvider('https://eth-goerli.g.alchemy.com/v2/3Cfhb0ZB3R-Lr_9FIpnI4mPouvQkUr0f'))


privateKey = "0d845b90a56f9e4709ba682e87be6a58417b27108c14ddeb7ab8c42251803559"

contract_addy = "0xb434C94BfEa3cBB682325dCDa927662fB9189A68"

addy = "0xBaFa7Da92715a1b06397bF26E6e335599769b412"


const fun = async () =>{
    var bal = await w3.eth.getBalance(addy)
    console.log(bal)
}

fun()