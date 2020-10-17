/**
 * Functions to change the output textarea and get the input textarea
 *
 * @author rick@gnous.eu
 * @licence GPL3
 */

/**
 * Set a text in a textarea with id output
 *
 * @param {string} outputText - text will be set in textarea
 */
function setOutputText(outputText) {
  let textArea = document.getElementById("output");
  textArea.value = outputText;
} 

/**
 * Parse the conf in the textarea with id input and print it in
 * textarea with id output
 */
function letsParse() {
  let textAreaValue = document.getElementById("input").value;
  let parsedText = parser.parseTxt(textAreaValue);
  setOutputText(parsedText);
}
