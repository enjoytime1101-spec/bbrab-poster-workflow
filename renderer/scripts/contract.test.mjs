import test from 'node:test';
import assert from 'node:assert/strict';
import {validate} from './contract.mjs';
const valid={brand:'BBRAB',title:'卫星任务',subtitle:'示例',accent:'#74d8cc',durationSeconds:6};
test('accept deterministic template fields',()=>assert.deepEqual(validate(valid),valid));
for(const [name,change] of Object.entries({duration:{durationSeconds:Infinity},overflow:{title:'a'.repeat(1000)},color:{accent:'url(http://x)'},unknown:{url:'http://x'},lines:{title:'one\ntwo\nthree'}})){
  test('reject '+name,()=>assert.throws(()=>validate({...valid,...change})));
}
