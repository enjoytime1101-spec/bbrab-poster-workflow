import {readFile,mkdir,writeFile,rename,unlink} from 'node:fs/promises';
import {resolve,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {createHash} from 'node:crypto';
import {bundle} from '@remotion/bundler';
import {selectComposition,renderMedia} from '@remotion/renderer';
import {validate} from './contract.mjs';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const [inputFile,outputFile]=process.argv.slice(2);
if(!inputFile||!outputFile||!outputFile.endsWith('.mp4'))throw Error('Usage: node scripts/render.mjs input.json output.mp4');
const props=validate(JSON.parse(await readFile(inputFile,'utf8')));
const out=resolve(outputFile);await mkdir(dirname(out),{recursive:true,mode:0o700});
const url=await bundle({entryPoint:resolve(root,'src/index.ts'),publicDir:resolve(root,'public')});
const browserExecutable=process.env.REMOTION_BROWSER_EXECUTABLE || null;
const composition=await selectComposition({browserExecutable,serveUrl:url,id:'BbrabMissionCard',inputProps:props});
const temporary=out+'.partial.mp4';
try{
 await renderMedia({browserExecutable,composition,serveUrl:url,codec:'h264',outputLocation:temporary,inputProps:props,concurrency:2,overwrite:false,timeoutInMilliseconds:60000});
 await rename(temporary,out);
 const bytes=await readFile(out);
 const report={ok:true,engine:'remotion',version:'4.0.534',composition:composition.id,width:composition.width,height:composition.height,frames:composition.durationInFrames,fps:composition.fps,bytes:bytes.length,sha256:createHash('sha256').update(bytes).digest('hex'),modelCalls:0};
 await writeFile(out+'.json',JSON.stringify(report,null,2)+'\n');console.log(JSON.stringify(report));
}catch(e){await unlink(temporary).catch(()=>{});throw e;}
