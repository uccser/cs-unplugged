/**                                                                           *
 *         A not necessarily secure class for encrypting JS strings           *
 *                                                                            *
 *              THE PURPOSE OF THIS MODULE IS NOT ENCRYPTION                  *
 *                                                                            *
 * This module is designed to help resolve any problem that could arise
 * from using an 'unencoded' string plainly
 */

// TODO:
// INCREMENT THIS NUMBER EACH TIME A CHANGE TO THE MODULE IS MADE THAT MIGHT
// BREAK EARLIER VERSIONS
const VERSION = 0;

/**
 * Uses an implementation of the Vigenère cipher to encode the given string with
 * the given key string.
 * 
 * Returns a pair (list) of the encoded string and the current version number
 */
function encode(s, key) {
  characters = s.split('');
  len = key.length;
  for (var i=0; i < characters.length; i++) {
    characters[i] = characters[i].charCodeAt(0) + key[i % len].charCodeAt(0);
  }
  return [String.fromCharCode(...characters), VERSION]; // ... is ES6 spread
}

/**
 * Uses an implementation of the Vigenère cipher to decode the given string with
 * the given key string
 * 
 * If the given version number does not match the current number, an exception is thrown.
 */
function decode(s, key, version) {
  if (version != VERSION) {
    throw "The given Scramble version '" + version + "' does not match the expected version '" + VERSION + "'.";
  }
  characters = s.split('');
  len = key.length;
  for (var i=0; i < characters.length; i++) {
    characters[i] = characters[i].charCodeAt(0) - key[i % len].charCodeAt(0);
  }
  return String.fromCharCode(...characters); // ... is ES6 spread
}

/**
 * Returns a random string of alphabetical characters of the given length
 * 
 * From https://stackoverflow.com/a/1349426
 */
function randomKey(length) {
  var result           = '';
  var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
  var charactersLength = characters.length;
  for ( var i = 0; i < length; i++ ) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength));
  }
  return result;
}

module.exports = {
  encode,
  decode,
  randomKey,
}
