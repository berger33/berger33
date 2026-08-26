const state={token:sessionStorage.getItem('chs_token')||'',user:null};
const $=s=>document.querySelector(s);
const $$=s=>[...document.querySelectorAll(s)];

async function api(path,options={}){
  const headers={...(options.headers||{})};
  if(state.token) headers.Authorization=`Bearer ${state.token}`;
  if(options.body && !(options.body instanceof FormData)) headers['Content-Type']='application/json';
  const response=await fetch(path,{...options,headers});
  if(response.status===204) return null;
  const isJson=(response.headers.get('content-type')||'').includes('application/json');
  const data=isJson?await response.json():await response.text();
  if(!response.ok) throw new Error(typeof data==='string'?data:JSON.stringify(data.detail||data));
  return data;
}

function showApp(user){state.user=user;$('#login').hidden=true;$('#app').hidden=false;$('#who').textContent=`${user.display_name} · ${user.role}`;showView('dashboard')}
function showLogin(){state.token='';state.user=null;sessionStorage.removeItem('chs_token');$('#app').hidden=true;$('#login').hidden=false}
function showView(id){$$('.view').forEach(v=>v.hidden=v.id!==id); if(id==='dashboard')loadDashboard(); if(id==='candidates')loadCandidates(); if(id==='vacancies')loadVacancies(); if(id==='audit')loadAudit()}

$('#loginForm').addEventListener('submit',async e=>{e.preventDefault();$('#loginError').textContent='';try{const data=await api('/api/auth/login',{method:'POST',body:JSON.stringify({username:$('#username').value,password:$('#password').value})});state.token=data.access_token;sessionStorage.setItem('chs_token',state.token);showApp(data.user)}catch(err){$('#loginError').textContent='Não foi possível entrar. Verifique as credenciais.'}});
$('#logout').addEventListener('click',async()=>{try{await api('/api/auth/logout',{method:'POST'})}finally{showLogin()}});
$$('[data-view]').forEach(button=>button.addEventListener('click',()=>showView(button.dataset.view)));

async function loadDashboard(){const d=await api('/api/dashboard');$('#dashboard').innerHTML=`<div class="section-head"><div><p class="eyebrow">VISÃO OPERACIONAL</p><h2>Dashboard</h2></div></div><div class="kpis">${[['Candidatos',d.candidates],['Novos',d.new_candidates],['Vagas abertas',d.open_vacancies],['Posições',d.open_positions],['Contratações',d.hires]].map(([l,v])=>`<div class="kpi"><span class="muted">${l}</span><strong>${v}</strong></div>`).join('')}</div><div class="section-head"><div><p class="eyebrow">FUNIL</p><h2>Etapas</h2></div><strong>${d.conversion_rate}% conversão</strong></div><div class="funnel">${Object.entries(d.funnel).map(([k,v])=>`<div><span class="muted">${k}</span><strong>${v}</strong></div>`).join('')||'<div>Nenhum candidato ainda.</div>'}</div>`}

function table(rows,columns){if(!rows.length)return'<div class="card">Nenhum registro encontrado.</div>';return`<table><thead><tr>${columns.map(c=>`<th>${c[0]}</th>`).join('')}</tr></thead><tbody>${rows.map(row=>`<tr>${columns.map(c=>`<td>${typeof c[1]==='function'?c[1](row):(row[c[1]]??'')}</td>`).join('')}</tr>`).join('')}</tbody></table>`}
async function loadCandidates(){const q=encodeURIComponent($('#candidateSearch').value||'');const rows=await api(`/api/candidates?q=${q}`);$('#candidateList').innerHTML=table(rows,[['Nome','name'],['Profissão','profession'],['Cidade','city'],['Status',r=>`<span class="badge">${r.status}</span>`],['Recrutador','recruiter']])}
$('#candidateSearch').addEventListener('input',()=>loadCandidates());
$('#candidateForm').addEventListener('submit',async e=>{e.preventDefault();const f=new FormData(e.currentTarget);const payload=Object.fromEntries(f.entries());payload.professional_registry='';payload.source='';payload.source_url='';payload.status='Novo';payload.notes='';payload.vacancy_id=null;try{await api('/api/candidates',{method:'POST',body:JSON.stringify(payload)});e.currentTarget.reset();await loadCandidates();await loadDashboard()}catch(err){alert(`Não foi possível salvar: ${err.message}`)}});

async function loadVacancies(){const rows=await api('/api/vacancies');$('#vacancyList').innerHTML=rows.length?rows.map(v=>`<article class="vacancy"><span class="badge">${v.status}</span><h3>${v.code} · ${v.title}</h3><p>${v.profession} · ${v.city||'Local não informado'}</p><p class="muted">${v.positions} posição(ões) · ${v.owner||'Sem responsável'}</p></article>`).join(''):'<div class="card">Nenhuma vaga cadastrada.</div>'}
$('#vacancyForm').addEventListener('submit',async e=>{e.preventDefault();const f=new FormData(e.currentTarget);const payload=Object.fromEntries(f.entries());payload.positions=Number(payload.positions||1);payload.status='aberta';try{await api('/api/vacancies',{method:'POST',body:JSON.stringify(payload)});e.currentTarget.reset();await loadVacancies();await loadDashboard()}catch(err){alert(`Não foi possível salvar: ${err.message}`)}});

async function loadAudit(){const rows=await api('/api/audit');$('#auditList').innerHTML=table(rows,[['Data',r=>new Date(r.created_at).toLocaleString('pt-BR')],['Usuário','actor'],['Ação','action'],['Entidade','entity'],['Detalhes','details']])}

(async()=>{if(!state.token)return;try{showApp(await api('/api/auth/me'))}catch{showLogin()}})();
