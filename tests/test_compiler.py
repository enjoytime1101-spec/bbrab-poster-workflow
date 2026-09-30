import copy, importlib.util, json, pathlib, tempfile, unittest
ROOT=pathlib.Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('compiler',ROOT/'skill/bbrab-poster-workflow/scripts/poster_workflow.py')
m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)

class CompilerTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.root=pathlib.Path(self.tmp.name)
  self.b=json.loads((ROOT/'examples/rocket-concept.json').read_text())
 def tearDown(self):self.tmp.cleanup()
 def compile(self):return m.compile_brief(self.b,self.root)
 def product(self):
  (self.root/'product.png').write_bytes(b'fixture-not-a-real-image')
  self.b['references']=[{'path':'product.png','role':'product','source':'synthetic fixture','rights_declared':True}]
 def test_complete_is_not_approved(self):
  r=self.compile();self.assertFalse(r['customer_accepted']);self.assertFalse(r['generation_connected']);self.assertEqual(r['status'],'awaiting_customer_confirmation');self.assertEqual(len(r['checks']),11)
 def test_partial_is_blocked(self):
  self.b.pop('holiday');self.assertEqual(self.compile()['status'],'blocked')
 def test_real_model_requires_all_evidence(self):
  self.b['accuracy_mode']='real_product';self.b['direction']='business'
  self.assertEqual(len(self.compile()['blockers']),3)
  self.b.update(model_name='Fictional test model',evidence_source='Test catalogue');self.product()
  self.assertEqual(self.compile()['blockers'],[])
 def test_bytes_and_brief_bind_id(self):
  self.product();a=self.compile()['plan_id'];(self.root/'product.png').write_bytes(b'changed');b=self.compile()['plan_id'];self.b['headline']='Changed';c=self.compile()['plan_id'];self.assertEqual(len({a,b,c}),3)
 def test_reference_not_falsely_decoded(self):
  self.product();self.assertIn('not_decoded',self.compile()['references'][0]['content_validation'])
 def test_path_escape_rejected(self):
  self.product();self.b['references'][0]['path']='../outside.png'
  with self.assertRaises(ValueError):self.compile()
 def test_symlink_escape_rejected(self):
  self.product();(self.root/'link.png').symlink_to(ROOT/'LICENSE');self.b['references'][0]['path']='link.png'
  with self.assertRaises(ValueError):self.compile()
 def test_rights_not_truthy(self):
  self.product();self.b['references'][0]['rights_declared']='true'
  with self.assertRaises(ValueError):self.compile()
 def test_dimensions(self):
  for value in (True,-1,10001,'1080'):
   self.b['width']=value;self.assertTrue(self.compile()['blockers'])
 def test_no_injected_approval_field(self):
  self.b['approved']=True
  with self.assertRaises(ValueError):self.compile()
 def test_subject_required(self):
  self.b['aerospace_subject']='unknown';self.assertTrue(self.compile()['blockers'])
 def test_concept_cannot_impersonate_product_direction(self):
  self.b['direction']='business';self.assertTrue(self.compile()['blockers'])
 def test_graph_edges(self):
  g=json.loads((ROOT/'workflow.json').read_text());ids={n['id'] for n in g['nodes']}
  for n in g['nodes']:
   for k,v in n.items():
    if k=='next' or k.startswith('on_'):self.assertIn(v,ids)
 def test_prompts_have_evaluation_boundaries(self):
  for c in json.loads((ROOT/'skill/bbrab-poster-workflow/references/prompts.json').read_text())['assets']:
   self.assertIsNone(c['model_evidence']);self.assertTrue(c['fallback'])

if __name__=='__main__':unittest.main()
