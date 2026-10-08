export function validate(input){
 if(!input||Array.isArray(input)||typeof input!=='object')throw Error('Expected a JSON object');
 const keys=['brand','title','subtitle','accent','durationSeconds'];
 if(Object.keys(input).some(k=>!keys.includes(k)))throw Error('Unsupported template field');
 for(const [key,max] of [['brand',32],['title',32],['subtitle',60]]){
  if(typeof input[key]!=='string'||!input[key].trim()||input[key].length>max||input[key].split('\n').length>2)throw Error(`Invalid ${key}: text exceeds safe layout bounds`);
 }
 if(!/^#[a-f\d]{6}$/i.test(input.accent))throw Error('Invalid accent');
 if(!Number.isFinite(input.durationSeconds)||input.durationSeconds<2||input.durationSeconds>30)throw Error('Duration must be 2–30 seconds');
 return {...input};
}
