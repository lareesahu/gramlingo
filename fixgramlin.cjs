const fs = require('fs');
const f = 'C:/Users/hunin/projects/gramlingo/src/screens/LearningPathScreen.tsx';
let c = fs.readFileSync(f, 'utf8');

// Find the cover image block and replace with Gramlin component
// Current:
// <div className=\"lp__img-wrap\">
//   <img src={coverSrc} alt={...} className=\"lp__img\" loading=\"lazy\" />
//   <span className=\"lp__spark lp__spark--1\">?</span>
//   ...
// </div>

// We want to replace the img with the Gramlin component
// The Gramlin import already exists

// Replace: <img src={coverSrc} ... /> with <Gramlin pose={mod.gramlin} size=\"lg\" />

// Find the img-wrap section
const imgWrapStart = '<div className=\"lp__img-wrap\">';
const imgWrapIdx = c.indexOf(imgWrapStart);
if (imgWrapIdx > -1) {
  // Find the closing of img-wrap
  const imgWrapEnd = c.indexOf('</div>', c.indexOf('<div className=\"lp__card-body\">', imgWrapIdx));
  
  // Extract the card-body to find where img-wrap ends and card-body begins
  const cardBodyIdx = c.indexOf('lp__card-body', imgWrapIdx);
  const imgWrapClose = c.lastIndexOf('</div>', cardBodyIdx);
  
  // Build replacement: Gramlin component instead of cover image + sparks
  const replacement = '<div className=\"lp__img-wrap lp__img-wrap--gramlin\">\n                    <Gramlin pose={mod.gramlin || \"book\"} size=\"lg\" />\n                  </div>';
  
  const before = c.substring(0, imgWrapIdx);
  const after = c.substring(imgWrapClose + '</div>'.length);
  c = before + replacement + after;
  
  console.log('replaced cover image with Gramlin pose');
} else {
  console.log('img-wrap not found');
}

fs.writeFileSync(f, c, 'utf8');
